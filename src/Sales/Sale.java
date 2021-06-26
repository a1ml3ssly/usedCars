package Sales;

import typeOfVehicles.Bike;
import typeOfVehicles.Car;
import typeOfVehicles.Vehicle;

import java.util.ArrayList;

public class Sale {
    ArrayList<Vehicle> vehicleArray;

    public Sale(){
        vehicleArray = new ArrayList<Vehicle>();
    }

    public void addCar(){
        vehicleArray.add(new Car());

        System.out.println("car has been added");
    }

    public void addBike(){
        vehicleArray.add(new Bike());
    }
}
