import java.util.Random;
import java.util.Scanner;

public class rockPaperScissors {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);


        String[] ai = new String[]{"Rock", "Paper","Scissors"};
        Random rand = new Random();

        int upperbound = 3;
        int int_random = rand.nextInt(upperbound);

        for(int i =0; i < 1; i++){
            System.out.println("Lets play Rock Paper Scissor");
            System.out.println("3");
            System.out.println("2");
            System.out.println("1");
            System.out.println("GOOOOOO");
            String input = sc.next();
            Logic(int_random,ai,input);
        }
    }
    static void Logic(int i, String[] ai, String player){
        if(ai[i].equals("Rock") && player.equals("Paper")){
            System.out.println("AI played Rock. You played Paper. You win");
        }
        if(ai[i].equals("Rock") && player.equals("Scissor")){
            System.out.println("AI played Rock. You played Paper. AI win");
        }
        if(ai[i].equals("Rock") && player.equals("Rock")){
            System.out.println("AI played Rock. You played Paper. Tie");
        }

        if(ai[i].equals("Paper") && player.equals("Paper")){
            System.out.println("AI played Paper. You played Paper. Tie");
        }
        if(ai[i].equals("Paper") && player.equals("Scissor")){
            System.out.println("AI played Scissor. You played Scissor. You win");
        }
        if(ai[i].equals("Paper") && player.equals("Rock")){
            System.out.println("AI played Paper. You played Rock. AI win");
        }

        if(ai[i].equals("Scissor") && player.equals("Paper")){
            System.out.println("AI played Scissor. You played Paper. AI wins");
        }
        if(ai[i].equals("Scissor") && player.equals("Scissor")){
            System.out.println("AI played Scissor. You played Scissor. Tie ");
        }
        if(ai[i].equals("Scissor") && player.equals("Rock")){
            System.out.println("AI played Scissor. You played Rock. You win");
        }


    }
}