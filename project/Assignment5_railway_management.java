                                   // Base Class
class Train {
    String trainName;
    int trainNumber;

    void setTrainDetails(String name, int number) {
        trainName = name;
        trainNumber = number;
    }

    void displayTrainDetails() {
        System.out.println("Train Name: " + trainName);
        System.out.println("Train Number: " + trainNumber);
    }
}

// Intermediate Class
class Reservation extends Train {
    String reservationDate;
    String seatNumber;

    void setReservationDetails(String date, String seat) {
        reservationDate = date;
        seatNumber = seat;
    }

    void displayReservationDetails() {
        System.out.println("Reservation Date: " + reservationDate);
        System.out.println("Seat Number: " + seatNumber);
    }
}

// Derived Class
class Passenger extends Reservation {
    String passengerName;
    int passengerAge;

    void setPassengerDetails(String name, int age) {
        passengerName = name;
        passengerAge = age;
    }

    void displayPassengerDetails() {
        System.out.println("Passenger Name: " + passengerName);
        System.out.println("Passenger Age: " + passengerAge);
    }
}

// Main Class
public class Assignment5_railway_management  {
    public static void main(String[] args) {
        Passenger p1 = new Passenger();

        // Setting values
        p1.setTrainDetails("Shatabdi Express", 12001);
        p1.setReservationDetails("2025-05-10", "B2-34");
        p1.setPassengerDetails("Sayani Dutta", 30);

        // Displaying values
        System.out.println("=== Railway Reservation Details ===");
        p1.displayTrainDetails();
        p1.displayReservationDetails();
        p1.displayPassengerDetails();
    }
}