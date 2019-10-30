# Data sources
database(
    thermoLibraries=['surfaceThermoPt', 'primaryThermoLibrary', 'thermo_DFT_CCSDTF12_BAC','DFT_QCI_thermo','C3','CH',],
    reactionLibraries = ['2015_Buras_C2H3_C4H6_highP'],
    seedMechanisms = [],
    kineticsDepositories = ['training'],
    kineticsFamilies =['surface', 'default'],
    kineticsEstimator = 'rate rules',)
catalystProperties(
    bindingEnergies = { # default values for Ni(111)
                       'C':(-6.045, 'eV/molecule'),  # Ni(111)
                       'H':(-2.352, 'eV/molecule'),  # Pt(111)
                       'O':(-4.712, 'eV/molecule'),  # Ni(111)
                       'N':(-4.352, 'eV/molecule'),
                       },
    surfaceSiteDensity=(2.72e-9, 'mol/cm^2'),
)

# List of species
species(
    label='X',
    reactive=True,
    structure=adjacencyList("1 X u0"),
)

species(
    label='C2H4',
    reactive=True,
    structure=SMILES("C=C"),
)

species(
    label='n-heptane',
    reactive=False,
    structure=SMILES("CCCCCCC"),
)

species(
    label='C4H8-1',
    reactive=True,
    structure=SMILES("CCC=C"),
)

species(
    label='C4H8-2',
    reactive=True,
    structure=SMILES("CC=CC"),
)

species(
    label='HX',
    reactive=True,
    structure=adjacencyList(
    """
    1 H u0 p0 c0 {2,S}
    2 X u0 p0 c0 {1,S}
    """
    )
)

# species(
#     label='C2H5X',
#     reactive=True,
#     structure=adjacencyList(
#     """
#     1 C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
#     2 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
#     3 H u0 p0 c0 {1,S}
#     4 H u0 p0 c0 {1,S}
#     5 H u0 p0 c0 {2,S}
#     6 H u0 p0 c0 {2,S}
#     7 H u0 p0 c0 {2,S}
#     8 X u0 p0 c0 {1,S}
#     """
#     )
# )

# species(
#     label='H',
#     reactive=True,
#     structure=SMILES("[H]"),
# )

# species(
#     label='C6H12-1',
#     reactive=True,
#     structure=SMILES("C=CCCCC"),
# )
#
# species(
#     label='C6H12-2',
#     reactive=True,
#     structure=SMILES("CC=CCCC"),
#  )
#
# species(
#     label='C6H12-3',
#     reactive=True,
#     structure=SMILES("CCC=CCC"),
# )
#
# species(
#     label='C6H12-1-3',
#     reactive=True,
#     structure=SMILES("C=CC(C)CC"),
# )
#
# species(
#     label='C6H12-2-3',
#     reactive=True,
#     structure=SMILES("CC=C(C)CC"),
# )

#----------
# Reaction systems
surfaceReactor(
    temperature=(423,'K'),
    initialPressure=(35, 'bar'),
    initialGasMoleFractions={
        "C2H4": 0.67,
        "n-heptane": 0.33,
    },
    initialSurfaceCoverages={
        "X": 1.0,
    },
    surfaceVolumeRatio=(1e7, 'm^-1'),  # should be 5.9e8, but when additional
    # ethylene is added in to maintain constant pressure so I'm making this less
    # so there is more ethylene than surface sites
    terminationTime=(100., 's'),
    #terminationRateRatio=1.e-3,
    terminationConversion={'C2H4': 0.9,}
    # terminationConversion={'X': 0.99,}
)

simulator(
    atol=1e-18,
    rtol=1e-12,
)

model(
    toleranceKeepInEdge=0.0,
    toleranceMoveToCore=1e-3,
    toleranceInterruptSimulation=1e-3,
    maximumEdgeSpecies=10000,
# PRUNING: uncomment to prune
    minCoreSizeForPrune=50,
# prune rxns from edge that dont move into core
    minSpeciesExistIterationsForPrune=3,
)

options(
    units='si',
    saveRestartPeriod=None,
    generateOutputHTML=True,
    generatePlots=False,
    saveEdgeSpecies=False,
    saveSimulationProfiles=True,
)

generatedSpeciesConstraints(
    allowed=['input species','reaction libraries'],
    maximumCarbonAtoms=14,
    maximumRadicalElectrons=0,
)
