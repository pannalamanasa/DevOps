package com.example;
import java.util.Scanner;

public class BMI {

    // Method to calculate BMI
    public static double calculateBMI(double weight, double height) {
        return Math.round((weight / (height * height)) * 100.0) / 100.0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter weight (kg): ");
        double weight = sc.nextDouble();
        System.out.print("Enter height (m): ");
        double height = sc.nextDouble();
        double bmi = calculateBMI(weight, height);
        System.out.println("Your BMI is: " + bmi);
        sc.close();
    }
}
