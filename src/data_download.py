import cdsapi
import os


def download_era5_land_data(output_path="../data/raw/era5_ro_1981_2024_land_monthly_means.nc"):
    """
    Downloads ERA5 Land monthly means data and saves it to a specified file path.

    Parameters:
        output_path (str): The full file path (including filename) to save the downloaded data.
                           Default is "../data/raw/era5_ro_1981_2024_land_monthly_means.nc".

    Returns:
        str: The file path of the downloaded NetCDF data.
    """

    # Ensure the output directory exists
    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")

    # Initialize the CDS API client (requires proper .cdsapirc configuration)
    client = cdsapi.Client()

    # Define the dataset and request parameters
    dataset = "reanalysis-era5-land-monthly-means"
    request = {
        "product_type": ["monthly_averaged_reanalysis"],
        "variable": [
            "2m_temperature",
            "volumetric_soil_water_layer_1",
            "surface_solar_radiation_downwards",
            "potential_evaporation",
            "total_precipitation"
        ],
        "year": [
            "1981", "1982", "1983",
            "1984", "1985", "1986",
            "1987", "1988", "1989",
            "1990", "1991", "1992",
            "1993", "1994", "1995",
            "1996", "1997", "1998",
            "1999", "2000", "2001",
            "2002", "2003", "2004",
            "2005", "2006", "2007",
            "2008", "2009", "2010",
            "2011", "2012", "2013",
            "2014", "2015", "2016",
            "2017", "2018", "2019",
            "2020", "2021", "2022",
            "2023", "2024"
        ],
        "month": [
            "01", "02", "03",
            "04", "05", "06",
            "07", "08", "09",
            "10", "11", "12"
        ],
        "time": ["00:00"],
        "data_format": "netcdf",
        "download_format": "unarchived",
        "area": [48.2655, 20.262, 43.6187, 29.7222]
    }

    # Retrieve the data and download it to the specified output path
    result = client.retrieve(dataset, request)
    result.download(output_path)
    print(f"Data downloaded and saved to {output_path}")
    return output_path


# Usage:
if __name__ == "__main__":
    file_path = "../data/raw/era5_ro_1981_2024_land_monthly_means.nc"
    download_era5_land_data(file_path)
