class Sailor{
    String name;
    int id;
    int fare;
    Sailor(String name,int id,int fare){ // parameterized constructor
        this.name=name;
        this.id=id;
        this.fare=fare;
    }
    
}
class Boat{
    String name;
    String type;
    int rent;
    Boat(String name,String type,int rent){ // parameterized constructor
        this.name=name;
        this.type=type;
        this.rent=rent;
    }
}
class Reserve{
    Sailor s;
    Boat b;
    String day;
    Reserve(Sailor s,Boat b,String day){
        this.s=s;
        this.b=b;
        this.day=day;
    }
    int calculateCost(String day){
        int cost = s.fare+b.rent;
        if(day=="Sunday"){
            cost=cost*2;
        }
        return cost;
    }
    void display(){
        
        System.out.println("Sailor Name :"+ s.name);
        System.out.println("Sailor id :"+ s.id);
        System.out.println("Boat Name :"+ b.name);
        System.out.println("Boat type :"+ b.type);
        System.out.println("Total cost :"+ calculateCost(day));
        
    }
    
}
public class Assignment1{
    public static void main(String [] args){
        
        Sailor s=new Sailor("jhon",1,200); 
        Boat b=new Boat("titanic","premium",500);
        String day="sunday";
        Reserve r=new Reserve(s,b,day);
        r.display();
        
    }
}