package typeOfVehicles;

public abstract class Vehicle {
    public String company;
    public String modelName;
    public String color;
    public int year;
    public String engineSize;
    public String fuelType;
    public String amountOfOwners;


    public abstract int getKilometers();

    public abstract void setKilometers(int kilometers);

    public abstract String getModelName();

    public abstract void setModelName(String modelName);

    public abstract String getColor();

    public abstract void setColor(String color);

    public abstract int getYear();

    public abstract void setYear(int year);

    public abstract String getEngineSize();

    public abstract void setEngineSize(String engineSize);

    public abstract String getFuelType();

    public abstract void setFuelType(String fuelType);

    public abstract String getAmountOfOwners();

    public abstract void setAmountOfOwners(String amountOfOwners);

}
