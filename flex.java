import java.util.Random;
import java.util.Scanner;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.Collections;
public class Flex {
    public static void main(String[] args) {
        Random random = new Random();
        
        // Generate a random integer between 0 and 100
        int randomInt = random.nextInt(101);
        System.out.println("Random Integer: " + randomInt);
        
        // Generate a random double between 0.0 and 1.0
        double randomDouble = random.nextDouble();
        System.out.println("Random Double: " + randomDouble);
        
        // Generate a random boolean value
        boolean randomBoolean = random.nextBoolean();
        System.out.println("Random Boolean: " + randomBoolean);
        
        // Generate random integers and print them
        for (int i = 0; i < 20; i++) {
            int randInt = random.nextInt(101);
            System.out.println("Random Integer " + i + ": " + randInt);
        }
        
        // Generate random doubles and print them
        for (int i = 0; i < 20; i++) {
            double randDouble = random.nextDouble();
            System.out.println("Random Double " + i + ": " + randDouble);
        }
        
        // Generate random booleans and print them
        for (int i = 0; i < 20; i++) {
            boolean randBoolean = random.nextBoolean();
            System.out.println("Random Boolean " + i + ": " + randBoolean);
        }
        
        // Generate random integers between 50 and 150
        for (int i = 0; i < 20; i++) {
            int randInt = 50 + random.nextInt(101);
            System.out.println("Random Integer between 50 and 150 " + i + ": " + randInt);
        }
        
        // Generate random doubles between 0.5 and 1.5
        for (int i = 0; i < 20; i++) {
            double randDouble = 0.5 + random.nextDouble();
            System.out.println("Random Double between 0.5 and 1.5 " + i + ": " + randDouble);
        }
        
        // Generate random integers between -100 and 100
        for (int i = 0; i < 20; i++) {
            int randInt = -100 + random.nextInt(201);
            System.out.println("Random Integer between -100 and 100 " + i + ": " + randInt);
        }
        
        // Generate random doubles between -1.0 and 1.0
        for (int i = 0; i < 20; i++) {
            double randDouble = -1.0 + 2 * random.nextDouble();
            System.out.println("Random Double between -1.0 and 1.0 " + i + ": " + randDouble);
        }
        
        // Additional random generation to reach 200 lines
        for (int i = 0; i < 20; i++) {
            int randInt = random.nextInt(1000);
            System.out.println("Random Integer between 0 and 1000 " + i + ": " + randInt);
        }
        
        for (int i = 0; i < 20; i++) {
            double randDouble = random.nextDouble() * 10;
            System.out.println("Random Double between 0.0 and 10.0 " + i + ": " + randDouble);
        }
        
        for (int i = 0; i < 20; i++) {
            boolean randBoolean = random.nextBoolean();
            System.out.println("Random Boolean " + i + ": " + randBoolean);
        }
    }
}
