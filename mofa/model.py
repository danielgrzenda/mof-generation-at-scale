from dataclasses import dataclass, field


@dataclass
class NodeDescription:
    """The inorganic components of a MOF"""

    name: str = ...
    """Human-readable name of the node (e.g., "Cu paddlewheel")"""
    xyz: str | None = None
    """XYZ coordinates of each atom in the node
    
    Uses At or Fr as an identifier of the the anchor points
    where the linkers attach to the node
    - At designates a carbon-carbon bond anchor
    - Fr designates other types of linkages
    """


@dataclass
class LigandDescription:
    """Description of organic sections which connect inorganic nodes"""

    name: str | None = ...
    """Human-readable name of the linker"""
    smiles: str = ...
    """SMILES-format designation of the molecule"""
    xyz: str | None = None
    """XYZ coordinates of each atom in the linker"""

    fragment_atoms: list[list[int]] | None = None
    """Groups of atoms which attach to the nodes
    
    There are typically two groups of fragment atoms, and these are 
    never altered during MOF generation."""

    @property
    def linker_atoms(self) -> list[int]:
        """All atoms which are not part of a fragment"""
        raise NotImplementedError()


@dataclass
class MOFRecord:
    """Information available about a certain MOF"""
    # Data describing what the MOF is
    identifiers: dict[str, str] = field(default_factory=dict)
    """Names of this MOFs is registries (e.g., hMOF)"""
    topology: str = ...
    """Description of the 3D network structure (e.g., pcu) as the topology"""
    catenation: int = ...
    """Degree of catenation. 0 corresponds to no interpenetrating lattices"""
    nodes: tuple[NodeDescription] = ...
    """Description of the nodes within the structure"""
    ligands: tuple[LigandDescription] = ...
    """Description of each linker within the structure"""

    # Information about the 3D structure of the MOF
    structure: str = ...
    """A representative 3D structure of the MOF in POSCAR format"""

    # Properties
    gas_storage: dict[tuple[str, float], float] = field(default_factory=dict)
    """Storage capacity of the MOF for different gases and pressures"""
    structure_stability: dict[str, float] = field(default_factory=dict)
    """How likely the structure is to be stable according to different assays
    
    A score of 1 equates to most likely to be stable, 0 as least likely."""
