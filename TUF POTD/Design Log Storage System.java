import java.util.*;

class LogSystem {

    private List<int[]> ids;
    private List<String> timestamps;

    public LogSystem() {
        ids = new ArrayList<>();
        timestamps = new ArrayList<>();
    }

    public void put(int id, String timestamp) {
        ids.add(new int[]{id});
        timestamps.add(timestamp);
    }

    public List<Integer> retrieve(String start, String end, String granularity) {

        Map<String, Integer> map = new HashMap<>();

        map.put("Year", 4);
        map.put("Month", 7);
        map.put("Day", 10);
        map.put("Hour", 13);
        map.put("Minute", 16);
        map.put("Second", 19);

        int len = map.get(granularity);

        String s = start.substring(0, len);
        String e = end.substring(0, len);

        List<Integer> ans = new ArrayList<>();

        for (int i = 0; i < timestamps.size(); i++) {

            String t = timestamps.get(i).substring(0, len);

            if (t.compareTo(s) >= 0 && t.compareTo(e) <= 0) {
                ans.add(ids.get(i)[0]);
            }
        }

        return ans;
    }
}