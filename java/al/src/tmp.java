
import java.io.*;
import java.util.ArrayList;
 
public class tmp {
    public static boolean[][] check;
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
         
        for (int t_c = 1; t_c <= T; t_c++) {
            int ans = 0;
            int N = Integer.parseInt(br.readLine());
            char[][] room = new char[N][N];
            check=new boolean[N][N];
            for (int i = 0; i < N; i++) {
                room[i] = br.readLine().toCharArray();
                for(int j=0;j<N;j++) {
                    if(room[i][j]=='W') {
                        check[i][j]=true;
                    }
                }
            }
            
            
            ArrayList<int[]> carpets = new ArrayList<>();
             
            for (int i = 0; i < N; i++) {
                loop1:for (int j = 0; j < N; j++) {
                    loop2:for (int h = 1; h <= N; h++) {
                        for (int w = 1; w <= N; w++) {
                            if (w*h == 1 || i+h > N || j+w > N)
                                continue;
                             
                            int ii = 0;
                            int jj = 0;
                            for (ii = i; ii < i+h; ii++) {
                                if (room[ii][j] == 'W')
                                    continue loop1;
                                for (jj = j; jj < j+w; jj++) {
                                    if (room[ii][jj] == 'W')
                                        continue loop2;
                                }
                            }
                            if (ii == i+h && jj == j+w)
                                carpets.add(new int[] {i, j, h, w});
                        }
                    }
                }
            }
             
            for (int i = 0; i < carpets.size(); i++) {
                int[] c1=carpets.get(i);
                cover(c1);
                for(int j=i+1;j<carpets.size();j++) {
                    int[] c2= carpets.get(j);
                    if(checkmate(c2)) {
                        ++ans;
                    }
                }
                coverout(c1);
                
            }
             
            System.out.println("#" + t_c + " " + ans%10007);
        }
         
    }
    private static void coverout(int[] c1) {
        int sy=c1[0];
        int sx=c1[1];
        int ey=c1[2];
        int ex=c1[3];
        for(int i=sy;i<sy+ey;i++) {
            for(int j=sx;j<sx+ex;j++) {
                check[i][j]=false;
            }
        }
         
    }
    private static boolean checkmate(int[] c2) {
        int sy=c2[0];
        int sx=c2[1];
        int ey=c2[2];
        int ex=c2[3];
        for(int i=sy;i<sy+ey;i++) {
            for(int j=sx;j<sx+ex;j++) {
                if(check[i][j]) {
                    return false;
                }
            }
        }
        return true;
    }
    private static void cover(int[] c1) {
        int sy=c1[0];
        int sx=c1[1];
        int ey=c1[2];
        int ex=c1[3];
        for(int i=sy;i<sy+ey;i++) {
            for(int j=sx;j<sx+ex;j++) {
                check[i][j]=true;
            }
        }
         
    }
     
}