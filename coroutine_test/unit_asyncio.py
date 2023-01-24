import asyncio
import itertools
import sys

async def spin(msg):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08'*len(status))
        try:
            #이벤트 블락하지 않고 sleep
            await asyncio.sleep(.1)
        #asyncio.CancelledError task 취소 > 루프 종료
        except asyncio.CancelledError:
            break
    write(' '*len(status)+'\x08'*len(status))

#slow_function = 코루틴 = await 문을 사용하여 I/O bound 작업하는 동안 이벤트 루프 진행
async def slow_function():
    #I/O 작업(sleep)끝나길 기다리고, 그동안 이벤트 루프는 계속 진행. 작업이 끝나면 slow_function 코루틴이 이 부분에서 이어서 진행
    await asyncio.sleep(3)
    return 42

#supervisor 함수도 코루틴
async def supervisor():
    #코루틴이 실행되도록 등록하고 Task 객체를 즉시 반환
    spinner = asyncio.ensure_future(spin('thinking!'))
    print('spinner object:', spinner)
    #await을 사용하여 asynceio.sleep의 실행이 종료될 때까지 이벤트 루프 진행
    result = await slow_function()
    #asyncio.sleep(3) 의 실행이 끝나면 await asynciio.sleep(3) 부분에서 코루틴이 재개하며, result 를 리턴해서 slow_function 의 실행이 끝나면, 마찬가지로 result = await slow_function() 부분에서 supervisor 코루틴이 재개된다. spinner.cancel 로 인해서 spin 코루틴의 await asyncio.sleep(.1) 부분에서 CancelledError 가 발생한다. 이 에러를 잡아서 처리하여 취소를 거부하도록 만들 수 있음
    spinner.cancel()
    return result

def main():
    loop = asyncio.get_event_loop()
    #이벤트 루프에 superviser 를 넣어서 끝날 때까지 실행시킨다.
    result = loop.run_until_complete(supervisor())
    loop.close()
    print('Answer: ', result)

if __name__=='__main__':
    main()
