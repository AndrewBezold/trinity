import ssz
from ssz.sedes import uint64

from eth2.beacon.typing import ValidatorIndex

from .block_headers import BeaconBlockHeader, default_beacon_block_header
from .defaults import default_validator_index


class ProposerSlashing(ssz.Serializable):

    fields = [
        # Proposer index
        ("proposer_index", uint64),
        # First block header
        ("header_1", BeaconBlockHeader),
        # Second block header
        ("header_2", BeaconBlockHeader),
    ]

    def __init__(
        self,
        proposer_index: ValidatorIndex = default_validator_index,
        header_1: BeaconBlockHeader = default_beacon_block_header,
        header_2: BeaconBlockHeader = default_beacon_block_header,
    ) -> None:
        super().__init__(
            proposer_index=proposer_index, header_1=header_1, header_2=header_2
        )
