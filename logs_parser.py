import argparse
import os
import re
import json
from collections import Counter
from heapq import nlargest


def logs_parser():
    parser = argparse.ArgumentParser(description='Log Analyzer')
    parser.add_argument(
        'directory',
        metavar='directory',
        type=str,
        help='Directory path containing log files',
    )

    args = parser.parse_args()

    analyze_logs(args.directory)


def analyze_log(log_file):
    stats = {
        'total_requests': 0,
        'request_methods': Counter(),
        'top_ips': Counter(),
        'top_requests': []
    }

    with open(log_file, 'r') as file:
        lines = file.readlines()

    for line in lines:
        ip_match = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
        if ip_match is not None:
            ip = ip_match.group()

            stats['top_ips'][ip] += 1

            request_method = re.search(r'\"(POST|GET|PUT|DELETE|HEAD)', line)
            if request_method is not None:
                request_method = request_method.group(1)

                stats['total_requests'] += 1
                stats['request_methods'][request_method] += 1

                request_url = re.findall(r'"([^"]+)"', line)[1]
                request_duration = re.search(r'\d+$', line).group()
                request_time = re.search(r'\[.*\]', line).group()[1:-1].split()[0]

                request = {
                    'method': request_method,
                    'url': request_url,
                    'ip': ip,
                    'duration': request_duration,
                    'datetime': request_time,
                }
                stats['top_requests'].append(request)

    stats['top_requests'] = nlargest(3, stats['top_requests'], key=lambda x: int(x['duration']))
    stats['top_ips'] = nlargest(3, stats['top_ips'].items(), key=lambda x: x[1])

    return stats


def save_stats(stats, output_file):
    with open(output_file, 'w') as file:
        json.dump(stats, file, indent=4)


def print_stats(stats):
    print('Total Requests:', stats['total_requests'])
    print('Request Methods:')
    for method, count in stats['request_methods'].items():
        print(f'{method}: {count}')
    print('Top IP Addresses:')
    for ip, count in stats['top_ips']:
        print(f'{ip}: {count}')
    print('Top Requests:')
    for request in stats['top_requests']:
        print('Method:', request['method'])
        print('URL:', request['url'])
        print('IP:', request['ip'])
        print('Duration:', request['duration'])
        print('Datetime:', request['datetime'])
        print()


def handle_stats(file_path: str):
    stats = analyze_log(file_path)
    output_file = os.path.splitext(file_path)[0] + '.json'
    save_stats(stats, output_file)
    print(f'Stats saved to {output_file}')

    print(f'\n===== {file_path} =====')
    print_stats(stats)
    print()


def analyze_logs(directory_or_file: str):
    if os.path.isdir(directory_or_file):
        log_files = [file for file in os.listdir(directory_or_file) if file.endswith('.log')]
        for log_file in log_files:
            file_path = os.path.join(directory_or_file, log_file)
            handle_stats(file_path)
    elif os.path.isfile(directory_or_file) and directory_or_file.endswith('.log'):
        file_path = directory_or_file
        handle_stats(file_path)
    else:
        print('Invalid input. Please provide a valid directory or file with .log extension.')


if __name__ == '__main__':
    logs_parser()
