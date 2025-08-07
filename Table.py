import pandas as pd
# from caas_jupyter_tools import display_dataframe_to_user

# Create a table of effectiveness-NTU formulas for different configurations
data = [
{
"Flow Arrangement": "Counterflow",
"Fluid Mixing": "Both unmixed",
"Use Case": "General fluids (sensible heat exchange)",
"Effectiveness (ε)": "ε = [1 - exp(-NTU*(1 - C_r))] / [1 - C_r*exp(-NTU*(1 - C_r))]",
"Notes": "C_r = C_min / C_max"
},
{
"Flow Arrangement": "Parallel flow",
"Fluid Mixing": "Both unmixed",
"Use Case": "General fluids (sensible heat exchange)",
"Effectiveness (ε)": "ε = [1 - exp(-NTU*(1 + C_r))] / [1 + C_r]",
"Notes": "C_r = C_min / C_max"
},
{
"Flow Arrangement": "One shell pass, multiple tube passes (Shell-and-tube)",
"Fluid Mixing": "Shell mixed, tubes unmixed",
"Use Case": "Liquid-liquid or steam-water exchangers",
"Effectiveness (ε)": "Use LMTD with correction factor F",
"Notes": "NTU method is not accurate, LMTD better"
},
{
"Flow Arrangement": "Crossflow",
"Fluid Mixing": "Both fluids unmixed",
"Use Case": "Air-cooled condenser, evaporator (e.g. round tube, plate fin coils)",
"Effectiveness (ε)": "ε = 1 - exp{-NTU^0.22 * [exp(-C_r * NTU^0.78) - 1] / C_r}",
"Notes": "Good for rectangular finned tube banks"
},
{
"Flow Arrangement": "Crossflow",
"Fluid Mixing": "Hot fluid unmixed, cold fluid mixed",
"Use Case": "Air cooling with large plenum or fan mixing",
"Effectiveness (ε)": "ε = 1 / C_r * [1 - exp(-C_r*(1 - exp(-NTU)))]",
"Notes": "Used for chilled water coils with mixed air"
},
{
"Flow Arrangement": "Condensation or evaporation (phase change)",
"Fluid Mixing": "N/A",
"Use Case": "Refrigerant side (condensation or boiling)",
"Effectiveness (ε)": "ε = 1 - exp(-NTU)",
"Notes": "Only one fluid has finite heat capacity"
},
{
"Flow Arrangement": "Crossflow",
"Fluid Mixing": "Both fluids mixed",
"Use Case": "Compact heat exchangers",
"Effectiveness (ε)": "ε = 1 - exp[-NTU * (1 + C_r)] / [1 + C_r]",
"Notes": "Less common"
}
]

df = pd.DataFrame(data)
display_dataframe_to_user("Effectiveness-NTU Formulas for Different Conditions", df)
