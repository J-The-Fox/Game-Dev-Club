package projects.examples.java;

import java.util.Scanner;

public class type_declaring {
    
    public static void main(String[] args){

    
        // Types Are Used To Store Data
        // There Are 8 Types In Java

        // This Is A String, It Can Store Text
        String myString = "Hello World!";
        System.out.println("String: " + myString);
        // This Is A boolean, It Can Store True Or False
        boolean myBoolean = true;
        System.out.println("boolean: " + myBoolean);
        // This Is A char, It Can Store A Single Character
        char myChar = 'a';
        System.out.println("char: " + myChar);
        // This Is A double, It Can Store Decimal Numbers From 4.9E-324 To 1.7976931348623157E308
        double myDouble = 5.5;
        System.out.println("double: " + myDouble);
        // This Is A float, It Can Store Decimal Numbers From 1.4E-45 To 3.4028235E38. Suffix The Number With f To Make It A float
        float myFloat = 5.2f;
        System.out.println("float: " + myFloat);
        // This Is An integer, It Can Store Whole Numbers From -2147483648 To 2147483647
        int myInt = 6;
        System.out.println("int: " + myInt);
        // This Is A byte, It Can Store Whole Numbers From -128 To 127
        byte myByte = 2;
        System.out.println("byte: " + myByte);
        // This Is A short, It Can Store Whole Numbers From -32768 To 32767
        short myShort = 1;
        System.out.println("short: " + myShort);
        // This Is A long, It Can Store Whole Numbers From -9223372036854775808 To 9223372036854775807
        long myLong = 8;
        System.out.println("long: " + myLong);

        // There Is Also A Type Called var, Which Is Used To Declare Variables But Have Java Automatically Determine The Type
        var myVar = "Hello World!"; // This Will Be A String
        System.out.println("var: " + myVar);

        // You Can Also Declare Variables Without Assigning Them A Value
        String myString2;
        
        // You Can Assign A Value To A Variable Later
        myString2 = "Hello World!";
        System.out.println("String Assigned Later: " + myString2);

        // You Can Also Declare Multiple Variables Of The Same Type On The Same Line
        String myString3, myString4;

        // You Can Also Declare Multiple Variables Of Different Types On The Same Line
        String myString5; int myInt2; boolean myBoolean2;

        // You Can Use Custom Types
        // This Is A Custom Type Called Scanner
        Scanner myCustomType = new Scanner(System.in);
        myCustomType.close();
    }
}
