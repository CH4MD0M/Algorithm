function solution(id_list, report, k) {
    const answer = [];
    const reports = [...new Set(report)].map((r) => {
        return r.split(" ");
    });

    const dict_reports = new Map();
    const check = new Map();

    for (let r of reports) {
        let condition = dict_reports.get(r[0]);
        dict_reports.set(r[0], condition ? [...condition, r[1]] : [r[1]]);
        check.set(r[1], check.get(r[1]) + 1 || 1);
    }

    for (let id of id_list) {
        let count = 0;
        for (let d in dict_reports.get(id)) {
            if (check.get(dict_reports.get(id)[d]) >= k) {
                count += 1;
            }
        }
        answer.push(count);
    }
    return answer;
}
