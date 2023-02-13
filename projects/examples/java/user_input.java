package projects.examples.java;

import java.util.Scanner;

public class user_input {
    
    public user_input(){
        // This Is The Constructer
        // It Always Has The Same Name As The Class
        // It Is Called When The Class Is Created
    }

    public static void main(String[] args){
        // This Is The Main Method
        System.out.println("This Is In The Main Method");

        Scanner scanner = new Scanner(System.in); // Create A Scanner

        System.out.println("Please Enter Something:");
        String input = scanner.nextLine(); // Get The User Input

        System.out.println("You Entered: " + input); // Print The User Input

        scanner.close(); // Close The Scanner
    }

}
