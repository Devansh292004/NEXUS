import unittest
from nexus.network_protocol_engine import PacketDSL, ProtocolFSMGenerator

class TestNetworkEngine(unittest.TestCase):
    def test_packet_dsl(self):
        dsl = PacketDSL()
        dsl.add_field("id", "uint8")
        dsl.add_field("payload", "bytes", 10)

        struct_code = dsl.generate_c_struct("Msg")
        self.assertIn("uint8_t id;", struct_code)
        self.assertIn("uint8_t payload[10];", struct_code)

        ser_code = dsl.generate_serialization("Msg")
        self.assertIn("buf[offset++] = pkt->id;", ser_code)
        self.assertIn("memcpy(buf + offset, pkt->payload, 10);", ser_code)

        deser_code = dsl.generate_deserialization("Msg")
        self.assertIn("pkt->id = buf[offset++];", deser_code)
        self.assertIn("memcpy(pkt->payload, buf + offset, 10);", deser_code)

    def test_fsm_generator(self):
        fsm = ProtocolFSMGenerator(["START", "END"], [{"from": "START", "event": 1, "to": "END"}])
        fsm_code = fsm.generate_c_fsm()
        self.assertIn("STATE_START", fsm_code)
        self.assertIn("STATE_END", fsm_code)
        self.assertIn("if (event == 1) return STATE_END;", fsm_code)

if __name__ == "__main__":
    unittest.main()
