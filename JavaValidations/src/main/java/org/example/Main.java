package org.example;
//generate  UUID code
import java.util.UUID;
//importing the scanner class
import java.util.Scanner;
//importing the file class
import java.io.File;
public class Main {
    public static void main(String[] args) {
        //creating a scanner object
        Scanner scanner = new Scanner(System.in);
        //asking the user to enter the file name
        System.out.println("Enter the file name: ");
        //storing the file name in a variable
        String fileName = scanner.nextLine();
        //creating a file object
        File file = new File(fileName);
        //checking if the file exists
        if (file.exists()) {
            //printing the file name
            System.out.println("File name: " + file.getName());
            //printing the absolute path
            System.out.println("Absolute path: " + file.getAbsolutePath());
            //printing the size
            System.out.println("Size: " + file.length());
        } else {
            //printing that the file does not exist
            System.out.println("The file does not exist.");
        }
        //closing the scanner object
        scanner.close();
    }
    //q: write an example to connect to database
    //a: https://www.tutorialspoint.com/jdbc/jdbc-sample-code.htm
    //q: write an example to generate UUID code
    //a: https://www.baeldung.com/java-uuid
}