import sys
from solution import init, numberOfCandidate, maxArea

CMD_INIT = 1
CMD_NUMBER_OF_CANDIDATE = 2
CMD_MAX_AREA = 3

def run():
    numQuery = int(sys.stdin.readline())
    isCorrect = False
    mMap = [[0 for _ in range(20)] for __ in range(20)]
    mStructure = [0 for _ in range(5)]
    
    for q in range(numQuery):
        inputs = iter(sys.stdin.readline().split())
        cmd = int(next(inputs))

        if cmd == CMD_INIT:
            N = int(next(inputs))
            for i in range(N):
                for j in range(N):
                    mMap[i][j] = int(next(inputs))
            init(N, mMap)
            isCorrect = True

        elif cmd == CMD_NUMBER_OF_CANDIDATE:
            M = int(next(inputs))
            for i in range(M):
                mStructure[i] = int(next(inputs))
            userAns = numberOfCandidate(M, mStructure)
            ans = int(next(inputs))
            if userAns != ans:
                isCorrect = False

        elif cmd == CMD_MAX_AREA:
            M = int(next(inputs))
            for i in range(M):
                mStructure[i] = int(next(inputs))
            mSeaLevel = int(next(inputs))
            userAns = maxArea(M, mStructure, mSeaLevel)
            ans = int(next(inputs))
            if userAns != ans:
                isCorrect = False

    return isCorrect

if __name__ == '__main__':
	sys.stdin = open('sample_input.txt', 'r')
	inputarray = input().split()
	TC = int(inputarray[0])
	MARK = int(inputarray[1])

	for testcase in range(1, TC + 1):
		score = MARK if run() else 0
		print("#%d %d" % (testcase, score), flush = True)