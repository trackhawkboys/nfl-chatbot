import java.net.*;
import java.io.*;


public class URLReader {
    public static void main(String[] args) throws Exception {
        String sportsio_url = ("https://api.sportsdata.io/v3/nfl/scores/json/Standings/2025?key=fac9abd4ba7f4433b90536d0612396f4");

        URL oracle = new URL(sportsio_url);
        BufferedReader in = new BufferedReader(
        new InputStreamReader(oracle.openStream()));

        String inputLine;
        while ((inputLine = in.readLine()) != null)
        in.close();
    }
}