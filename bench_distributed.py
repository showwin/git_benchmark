import datetime
import os
import random

BENCH_DIR = './benchmark_dir'
GIT_INIT = 'git init > /dev/null'
GIT_ADD = 'git add --all'
GIT_COMMIT = 'git commit -m "git bench" > /dev/null'

def clean():
    os.system('rm -rf ./.git')
    os.system('rm -rf {}'.format(BENCH_DIR))
    os.system('mkdir {}'.format(BENCH_DIR))


def initialize():
    os.system('git init')


def generate_and_commit():
    filename = 'file' + str(random.randint(1, 5000))
    content = {}
    for i in range(10):
        content[i] = i
    content[random.randint(0, 9)] = 100
    gen_dir = os.path.join(BENCH_DIR, filename)
    if not os.path.exists(gen_dir):
        os.system('mkdir {0} && cd {0} && {init}'.format(gen_dir, init=GIT_INIT))
    os.system('echo {} > {}/{}'.format(content, gen_dir, filename))
    os.system('cd {dir} && {add} && {commit}'.format(
        dir=gen_dir,
        add=GIT_ADD,
        commit=GIT_COMMIT
    ))


def main():
    clean()
    print('cleaned')
    initialize()
    print('initialized')
    start_time = datetime.datetime.now()
    print('start benchmark')
    for _ in range(20):
        batch_start = datetime.datetime.now()
        for _ in range(1000):
            generate_and_commit()
        batch_end = datetime.datetime.now()
        duration = batch_end - batch_start
        print(duration, 1000 / duration.total_seconds())
    end_time = datetime.datetime.now()
    print(end_time - start_time)


if __name__ == '__main__':
    main()
