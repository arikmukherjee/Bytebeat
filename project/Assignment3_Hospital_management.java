                                                                                                                                                             //Write a program in Java for Hospital management using Multilevel inheritance with at least 3 classes all classes must have two-member 
//variable and two-member method.

class Hospital{
    String hospitalName;
	String location;

    void setHospitalName(String name,String loc){
        this.hospitalName= name;
        this.location= loc;
    }

    void displayDetails(){
        System.out.println("Hopital name : " + hospitalName);
        System.out.println("LOcation : "+location);
    }
}

class Department extends Hospital{
    String deptName;
    String hod;

    void deptDetails(String deptName, String hod){
        this.deptName=deptName;
        this.hod=hod;
    }

    void displayDeptDetails(){
        System.out.println("Department name : " +deptName);
        System.out.println("Head Of The Department : "+hod);
    }
}

class Doctors extends Department{
    String docName;
    String specialization;

    void docDetails( String name,String speciality){
       this.docName=name;
       this.specialization=speciality;
    }

    void displayDocDetails(){
        System.out.println("Doctor's name : " +docName);
        System.out.println("\nHis/Her specialization : "+specialization);
    }
}

public class Assignment3_Hospital_management{
    public static void main(String[] arg){
        Doctors doc = new Doctors();
        doc.setHospitalName("B.N.Bose","BKP");
        doc.deptDetails("Neurosurgeon","Dr. Christine Palmer");
        doc.docDetails("Dr. Strange","Neurourgery");

        doc.displayDetails();
        doc.displayDeptDetails();
        doc.displayDocDetails();
    }
}
