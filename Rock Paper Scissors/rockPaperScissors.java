import java.util.Random;
import java.util.Scanner;

public class rockPaperScissors {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        String[] options = {"Rock", "Paper", "Scissors"};

        while (true) {
            System.out.println("Enter your choice (Rock, Paper, Scissors) or type 'exit' to end: ");
            String userChoice = scanner.nextLine().toLowerCase();

            if (userChoice.equals("exit")) {
                System.out.println("Thanks for playing! Exiting the game.");
                break;
            }

            if (!userChoice.equals("rock") && !userChoice.equals("paper") && !userChoice.equals("scissors")) {
                System.out.println("Invalid choice. Please enter Rock, Paper, or Scissors.");
                continue;
            }

            int computerIndex = random.nextInt(3);
            String computerChoice = options[computerIndex];

            System.out.println("Computer chose: " + computerChoice);

            // Determine the winner
            if (userChoice.equals(computerChoice.toLowerCase())) {
                System.out.println("It's a tie!");
            } else if ((userChoice.equals("rock") && computerChoice.equals("Scissors"))
                    || (userChoice.equals("paper") && computerChoice.equals("Rock"))
                    || (userChoice.equals("scissors") && computerChoice.equals("Paper"))) {
                System.out.println("You win!");
            } else {
                System.out.println("Computer wins!");
            }
        }
    }
}