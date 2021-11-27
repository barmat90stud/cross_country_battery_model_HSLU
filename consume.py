#!/usr/bin/env python
import faust


class Test(faust.Record):
    Session: str
    time: str
    bpm: str
    br: str
    hrv: str
    ibi: str
    EventTimestamp: int


app = faust.App("hello-word", broker="kafka://86.119.35.243:9092")
topic = app.topic("test", value_type=Test)


@app.agent(topic)
async def process(stream):
    async for event in stream:
        print(f"Received: {event!r}")


if __name__ == "__main__":
    app.main()
