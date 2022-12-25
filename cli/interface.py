from main import run
import sys

args = sys.argv[1:]

runArgs = {
    'host' : '127.0.0.1',
    'port' : 8888,
}

for i in range(len(args) - 1):
    if args[i][0] == '-':
        match args[i]:
            case '-h':
                runArgs['host'] = str(args[i + 1])
                continue
            case '-p':
                runArgs['port'] = int(args[i + 1])
                continue
            case _:
                print("Error: undefined argument")

run(runArgs)