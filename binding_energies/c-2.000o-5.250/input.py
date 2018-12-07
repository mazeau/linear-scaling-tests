# Data sources
database(
    thermoLibraries=['surfaceThermoPt', 'primaryThermoLibrary', 'thermo_DFT_CCSDTF12_BAC','DFT_QCI_thermo'],
    reactionLibraries = [('CPOX_Pt/Deutschmann2006', True)],
    seedMechanisms = [],
    kineticsDepositories = ['training'],
    kineticsFamilies =['surface','default'],
    kineticsEstimator = 'rate rules',
    bindingEnergies = { # default values for Pt(111)
                       'C':(-2.000000, 'eV/molecule'),
                       'H':(-2.778, 'eV/molecule'),
                       'O':(-5.250000, 'eV/molecule'),
                       }
)

# List of species
species(
    label='X',
    reactive=True,
    structure=adjacencyList("1 X u0"),
)

species(
    label='He',
    reactive=True,
    structure=adjacencyList("1 He u0 p1 c0"),
)

species(
    label='CH4',
    reactive=True,
    structure=SMILES("[CH4]"),
)

species(
    label='H2',
    reactive=True,
    structure=SMILES("[H][H]"),
)

species(
    label='C2H6',
    reactive=True,
    structure=SMILES("CC"),
)

species(
    label='CH3',
    reactive=True,
    structure=SMILES("[CH3]"),
)

species(
    label='C3H8',
    reactive=True,
    structure=SMILES("CCC"),
)

species(
    label='H',
    reactive=True,
    structure=SMILES("[H]"),
)

species(
    label='C2H5',
    reactive=True,
    structure=SMILES("C[CH2]"),
)

species(
    label='C4H8',
    reactive=True,
    structure=SMILES("C=CCC"),
)

species(
    label='C2H4',
    reactive=True,
    structure=SMILES("C=C"),
)

#----------
# Reaction systems
surfaceReactor(
    temperature=(353,'K'),
    initialPressure=(31.0, 'bar'),
    initialGasMoleFractions={
        "C2H4": 0.5,
        "He": 0.5,
    },
    initialSurfaceCoverages={
        "X": 1.0,
    },
    surfaceVolumeRatio=(1.e5, 'm^-1'),
    surfaceSiteDensity=(2.9e-9, 'mol/cm^2'),
#    terminationConversion = { "CH4":0.9,},
    terminationTime=(1000., 's'),
#    terminationConversion={'C2H4': 0.99,}
)

simulator(
    atol=1e-18,
    rtol=1e-12,
)

model(
    toleranceKeepInEdge=0.0,
    toleranceMoveToCore=1e-4,
    toleranceInterruptSimulation=0.1,
    maximumEdgeSpecies=100000
)

options(
    units='si',
    saveRestartPeriod=None,
    generateOutputHTML=True,
    generatePlots=False,
    saveEdgeSpecies=True,
    saveSimulationProfiles=True,
)
