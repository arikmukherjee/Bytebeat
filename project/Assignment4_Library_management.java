                               
class Library{
    String LibraryName;
	String location;

    void setLibraryName(String name,String loc){
        this.LibraryName= name;
        this.location= loc;
    }

    void displayDetails(){
        System.out.println("Library name: " + LibraryName);
        System.out.println("LOcation: "+location);
    }
}

class Book extends Library {
    String bookTitle;
    String bookAuthor;

    void setBookDetails(String title, String author) {
        bookTitle = title;
        bookAuthor = author;
    }

    void displayBookDetails() {
        System.out.println("Book Title: " + bookTitle);
        System.out.println("Book Author: " + bookAuthor);
    }
}

class available_books_Genre extends Book{
    String fantasy;
    String non_fiction;
    String horror;
    String SCI_FI;
    String Historical_Fiction;

    void books(String fantasy,String non_fiction,String horror,String SCI_FI,String Historical_Fiction){
        this.fantasy=fantasy;
        this.non_fiction=non_fiction;
        this.horror=horror;
        this.SCI_FI=SCI_FI;
        this.Historical_Fiction = Historical_Fiction;
    }

    void displaybooknames(){
        System.err.println("available books are:\n");
        System.out.println("fantasy book genre : " +fantasy);
        System.out.println("horror book genre : " +horror);
        System.out.println("non_fiction book genre : " +non_fiction);
        System.out.println("SCI_FI book genre : " +SCI_FI);
        System.out.println("Historical_Fiction book genre : "+Historical_Fiction);
    }
}

class details extends available_books_Genre{
    String readerName;
    int readerid;
    String issueDate;
    String returnDate;

    void readerDetails(String name,int id){
       this.readerName=name;
       this.readerid=id;
    }

    void issue_and_return_date(String issue,String ret){
        this.issueDate=issue;
        this.returnDate=ret;
    }

    void displayreaderDetails(){
        System.out.println("reader name: " +readerName);
        System.out.println("His/Her id: "+readerid);
    }

    void display_issue_and_return_date(){
        System.out.println("Issuance date: "+issueDate);
        System.out.println("return Date: "+returnDate);
    }

    void check_return(){
        if (returnDate==null){
            System.out.println("Not returned");
        }
        else{
            System.err.println("returned");
        }
    }
}

public class Assignment4_Library_management {
    public static void main(String[] args) {
        details reader = new details();
        reader.setLibraryName("Hgwarts","Hogsmeade");
        reader.setBookDetails("Fourth wing","Rebecca Yarros");
        reader.books("Fourth Wing","Stealing Fire","Dracula","The Time Machine","Kalermondira");
        reader.readerDetails("Sayani Dutta",111);
        reader.issue_and_return_date("2025-05-01","2025-05-08");
        reader.displayDetails();
        reader.displayBookDetails();
        reader.displaybooknames();
        reader.displayreaderDetails();
        reader.display_issue_and_return_date();
        reader.check_return();
    }
}
