import os
import sys

def main():
    cwd = os.getcwd()
    print(cwd)
    os.chdir("../../")
    cwd = os.getcwd()
    print(cwd)
    path = os.path.join(cwd,'deployment/llmops-helper',sys.argv[1])
    with open(path, 'r') as f:
        output = f.read()

    start = output.find('"name": "') + len('"name": "')
    end = output.find('"', start)

    name = output[start:end]
    return name

if __name__ == "__main__":
    run_name = main()
    print(run_name)
    