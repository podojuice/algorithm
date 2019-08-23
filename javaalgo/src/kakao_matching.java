import java.util.HashMap;
import java.util.HashSet;
import java.util.Arrays;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
class kakao_matching{
    private static final Pattern URL_PATTERN = Pattern.compile("<meta property=\"og:url\" content=\"https://(.+?)\"/>");
    private static final Pattern EXTERNAL_LINK = Pattern.compile("<a href=\"https://(.+?)\">");
    private HashMap<String, Page> pageMap = new HashMap<>();
 
    private class Page {
        private HashSet<String> hadExternalLinks = new HashSet<>();
        private HashSet<String> externalLinks = new HashSet<>();
        private String html;
        private String word;
        private String url;
        private int defaultScore = 0;
        public int id;
 
        public Page(String word, String html, int id) {
            this.word = word;
            this.html = html;
            this.id = id;
            initUrl();
            initDefaultScore();
        }
 
        private void initDefaultScore() {
            int find = html.indexOf(word);
            while (find != -1)
            {
                Character[] wordBorder = { html.charAt(find - 1), html.charAt(find + word.length()) };
                if (Arrays.stream(wordBorder).anyMatch(ch -> ch.charValue() >= 'a' && ch.charValue() <= 'z') == false)
                    defaultScore++;
                find = html.indexOf(word, find + 1);
            }
        }
 
        private void initUrl() {
            Matcher matcher = URL_PATTERN.matcher(html);
            while (matcher.find())
                url = matcher.group(1);
        }
 
        public double getTotalScore() {
            double ret = defaultScore;
            for (String link : externalLinks) {
                if (pageMap.containsKey(link)) {
                    Page externalPage = pageMap.get(link);
                    if (externalPage.hadExternalLinks.size() > 0)
                        ret += (double) externalPage.defaultScore / externalPage.hadExternalLinks.size();
                }
            }
            return ret;
        }
 
        public void initExternalLink() {
            Matcher matcher = EXTERNAL_LINK.matcher(html);
            while (matcher.find()) {
                String link = matcher.group(1);
                if (hadExternalLinks.contains(link) == false)
                    hadExternalLinks.add(link);
                if (pageMap.containsKey(link))
                    pageMap.get(link).externalLinks.add(url);
            }
        }
    }
 
    public int solution(String word, String[] pages) {
        int id = 0;
        for (String html : pages) {
            Page page = new Page(word.toLowerCase(), html.toLowerCase(), id);
            pageMap.put(page.url, page);
            id++;
        }
        for (Page page : pageMap.values()) {
            page.initExternalLink();
        }
        return pageMap.values().stream().max((a, b) -> Double.compare(a.getTotalScore(), b.getTotalScore())).get().id;
    }
}
