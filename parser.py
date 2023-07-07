from datetime import datetime
from subprocess import run


def run_parser():
    current_time = datetime.now()
    filename = current_time.strftime('%d-%m-%Y-%H.%M-scan.txt')

    result = run(['ps', 'aux'], capture_output=True, text=True)
    output = result.stdout
    lines = output.split('\n')

    users = set()
    total_processes = len(lines) - 2
    user_processes = {}

    for line in lines[1:-1]:
        fields = line.split()
        user = fields[0]
        users.add(user)
        user_processes[user] = user_processes.get(user, 0) + 1

    total_memory = sum(float(fields[5]) for line in lines[1:-1] for fields in [line.split()])
    total_cpu = sum(float(fields[2]) for line in lines[1:-1] for fields in [line.split()])

    max_memory_process = max(lines[1:-1], key=lambda process: float(process.split()[5]))
    max_cpu_process = max(lines[1:-1], key=lambda process: float(process.split()[2]))

    report = f'Отчёт о состоянии системы:\n'
    report += f'Пользователи системы: {", ".join(users)}\n'
    report += f'Процессов запущено: {total_processes}\n'
    report += f'Пользовательских процессов:\n'
    for user, process_count in user_processes.items():
        report += f'{user}: {process_count}\n'
    report += '...\n'
    report += f'Всего памяти используется: {total_memory:.1f} mb\n'
    report += f'Всего CPU используется: {total_cpu:.1f}%\n'
    report += f'Больше всего памяти использует: {max_memory_process.split()[10][:20]}\n'
    report += f'Больше всего CPU использует: {max_cpu_process.split()[10][:20]}\n'

    print(report)

    with open(filename, 'w') as file:
        file.write(report)


if __name__ == '__main__':
    run_parser()
