import mido
import time
from collections import deque

print(mido.get_output_names())
print(mido.get_input_names())

inport = mido.open_input('NUX MIGHTY LITE MIDI:NUX MIGHTY LITE MIDI Bluetooth 128:0')
outport = mido.open_output('NUX MIGHTY LITE MIDI:NUX MIGHTY LITE MIDI Bluetooth 128:0')

msglog = deque()

drumOn = mido.Message('control_change', channel=0, control=122, value=127, time=0)
outport.send(drumOn)

# while True:
#     msg = inport.receive()
#     if msg.type != "clock":
#         print(msg)
#         msglog.append({"msg": msg, "due": time.time() + echo_delay})
