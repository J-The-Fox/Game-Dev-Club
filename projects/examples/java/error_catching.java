package projects.examples.java;

public class error_catching {
    // This Is The Class

    public static void main(String[] args) {
        // This Is The Main Method

        // This Is A Try-Catch Block
        // This Is The Try Block, It Will Try To Run This Code
        try {
            int[] myNumbers = {1, 2, 3};
            System.out.println(myNumbers[10]);
            // This Will Throw An Error, Because There Is No Value At Index 10
        
        }
        // This Is The Catch Block, It Will Run If The Try Block Throws An Error
        catch (Exception e) {
            System.out.println("Something Went Wrong!");
        }


        // You Can Catch More Specific Errors As Well
        try {
            int[] myNumbers = {1, 2, 3};
            System.out.println(myNumbers[10]);
        }
        // This Is The Catch Block For ArrayIndexOutOfBoundsException, Which Is The Error That Will Be Thrown
        catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Something Went Wrong!");
        }

        // You Can Also Catch Multiple Errors In One Catch Block
        try {
            int[] myNumbers = {1, 2, 3};
            System.out.println(myNumbers[10]);
        }
        // This Is The Catch Block For ArrayIndexOutOfBoundsException And NullPointerException, Which Are The Errors That Will Be Thrown
        catch (ArrayIndexOutOfBoundsException | NullPointerException e) {
            System.out.println("Something Went Wrong!");
        }

        // You Can Also Use Them In Separate Catch Blocks
        try {
            int[] myNumbers = {1, 2, 3};
            System.out.println(myNumbers[10]);
        }
        // This Is The Catch Block For ArrayIndexOutOfBoundsException, Which Is The Error That Will Be Thrown
        catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Something Went Wrong!");
        }
        // This Is The Catch Block For NullPointerException, Which Is Another Error That Will Be Thrown
        catch (NullPointerException e) {
            System.out.println("Something Went Wrong!");
        }

        // You Can Print The Error Message With The Exception Object
        try {
            int[] myNumbers = {1, 2, 3};
            System.out.println(myNumbers[10]);
        }
        // This Is The Catch Block, It Will Run If The Try Block Throws An Error
        catch (Exception e) {
            System.out.println("Something Went Wrong!");
            System.out.println(e.getMessage());
        }

        // You Can Also Use A Finally Block
        // This Is The Try Block, It Will Try To Run This Code
        try {
            int[] myNumbers = {1, 2, 3};
            System.out.println(myNumbers[10]);
        }
        // This Is The Catch Block, It Will Run If The Try Block Throws An Error
        catch (Exception e) {
            System.out.println("Something Went Wrong!");
        }
        // This Is The Finally Block, It Will Run No Matter What
        finally {
            System.out.println("The Final Try-Catch Block Finished!");
        }
    }
}
