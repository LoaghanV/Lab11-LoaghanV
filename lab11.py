# Intermediate programming practice: async and sockets.
#
# For EACH problem, work out your problem-solving OUTLINE first, then implement it (you
# may use an AI assistant to help - see the README). The async parts must actually run
# their work CONCURRENTLY (that's the whole point), not one after another.
#
# Do not rename the functions - the tests use these names.

import asyncio
import socket


async def gather_doubled(numbers):
    # Outline (write your plan here first):
    '''
    I need to make a async function that takes a number/numbers and returns them doubled.
    Then I need to use .gather to return the list after all the computations are done.
    '''
    #   ...
    # TODO (Part 1, async): run one async task per number that returns n * 2, all
    #   CONCURRENTLY with asyncio.gather, and return the results as a list in the same
    #   order as `numbers`.
    async def double(num):
        return num * 2
    
    return await asyncio.gather(*(double(n) for n in numbers))


async def fastest(jobs):
    # Outline:
    '''
    I need to make a async function to start all the jobs and I'll have to use .sleep(delay) to pause them all
    for their set amount of time. Then I'll return the label once the time runs out.
    Lastly, I'll use as_completed and a for loop to return the value of the first label completed
    '''
    #   ...
    # TODO (Part 2, async): `jobs` is a list of (label, delay) pairs. Start them all
    #   concurrently - each one just does `await asyncio.sleep(delay)` - and return the
    #   label of the FIRST job to finish. (Hint: asyncio.as_completed.)
    async def startJob(label, delay):
        await asyncio.sleep(delay)
        return label

    for completed in asyncio.as_completed([startJob(label, delay) for label, delay in jobs]):
        return await completed
    


def echo_once(host, port, message):
    # Outline:
    '''
    First, I'll have to open a socket using socket.socket
    Next, I'll have to connect to a port using .connect and the tupple (host, port)
    I'll have to send a message as bytes to the server using encode and sendall
    Lastly, I'll have to recieve bytes back with recv and decode
    '''
    #   ...
    # TODO (Part 3, sockets): open a TCP socket and connect to (host, port). Send
    #   `message` (encode it to bytes first), receive the server's reply, and return it
    #   as a string. (Hint: socket.socket, .connect, .sendall, .recv, .decode.)
    with socket.socket() as client:
        client.connect((host, port))
        client.sendall(message.encode())
        reply = client.recv(1024)
        return reply.decode()


def main():
    # Optional scratch space - try the async parts here, e.g.:
    print(asyncio.run(gather_doubled([1, 2, 3, 4])))   # [2, 4, 6, 8]
    print(asyncio.run(fastest([("A", 0.06), ("B", 0.02), ("C", 0.04)])))   # returns "B"
    #doesnt work because "target machine actively refused it"
    print(echo_once("127.0.0.1", 50011, "hello"))   # returns "hello"   (against an echo server)



if __name__ == "__main__":
    main()
