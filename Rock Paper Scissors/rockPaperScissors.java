import java.util.Random;
import java.util.Scanner;

public class rockPaperScissors {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        String[] options = {"Rock", "Paper", "Scissors"};

        while (true) {
            System.out.println("Enter your choice (Rock, Paper, Scissors) or type 'exit' to end: ");
            String input = scanner.nextLine().toLowerCase();

            if (input.equals("exit")) {
                System.out.println("Thanks for playing! Exiting the game.");
                break;
            }

            if (!input.equals("rock") && !input.equals("paper") && !input.equals("scissors")) {
                System.out.println("Invalid choice. Please enter Rock, Paper, or Scissors.");
                continue;
            }

            int computerIndex = random.nextInt(3);
            String computerChoice = options[computerIndex];

            System.out.println("Computer chose: " + computerChoice);

            // Determine the winner
            if (input.equals(computerChoice.toLowerCase())) {
                System.out.println("It's a tie!");
            } else if ((input.equals("rock") && computerChoice.equals("Scissors"))
                    || (input.equals("paper") && computerChoice.equals("Rock"))
                    || (input.equals("scissors") && computerChoice.equals("Paper"))) {
                System.out.println("You win!");
            } else {
                System.out.println("Computer wins!");
            }
        }
    }
}