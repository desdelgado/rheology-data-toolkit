"""Schemas for polyelectrolyte rheology data and metadata

Gets the meta data in a json file to be put in the HDF5 file
"""


from pydantic import BaseModel, Field, AnyUrl

class BatteryMetadata(BaseModel):
    """
    Representation for the metadata about about a rheological run 
    on a polyelectrolyte system.  A complete set of metadata should be sufficient to 
    reproduce an experiment.
    """

    # TODO (delgadode): Make this general to rheological experiments and then add in 
    # section for polyelectrolytes
    # TODO (delgadode): Make schema for frequency sweep 

    name: str = Field(None, description="Name of the test.  Any form for the name is acceptable,"
                                        " as long as it is inteded to be used by the rheology data provider")

    comments: str = Field(None, description="Long form comments describing the test")

    # Fields that describe the test protocol
    type_of_test: str = Field(None, description="Type of test conducted")
    temperature: float = Field(None, description="Temperature of experiment")
    frequency_start: float = Field(None, description="Starting fequency of frequency sweep")
    frequency_stop: float = Field(None, description="Stopping fequency of frequency sweep")
    strain_amplitude: float = Field(None, description="Strain aplitude used during test")


    # Field that describe the polyelectrolytes
    polyanion: str = Field(None, description="Full name of polyanion used")
    polycation: str = Field(None, description="Full name of polycation used")

    polyanion_mw: float = Field(None, description="Molecular weight of polyanion")
    polycation_mw: float = Field(None, description="Molecular of polycation")

    polyanion_cf: float = Field(None, description="Charge fraction of polyanion")
    polycation_cb: float = Field(None, description="Charge fraction of polycation")

    salt: str = Field(None, description="Salt used in solution")
    solvent: str Field(None, description="Solvent used in solution")

    stoichiometric_ratio: float = Field(None, description="Ratio of polyanion/cation")
    



