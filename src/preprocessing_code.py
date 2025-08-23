import xarray as xr


def load_dataset(file_path):
    ds = xr.open_dataset(file_path)
    return ds
