using Pkg

Pkg.add([
    PackageSpec(name="NCDatasets"),
    PackageSpec(name="DifferentialEquations"),
])
Pkg.precompile()
