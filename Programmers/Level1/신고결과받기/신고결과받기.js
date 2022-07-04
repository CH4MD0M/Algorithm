function solution(id_list, report, k) {
    const reports = [...new Set(report)].map((r) => {
        return r.split(" ");
    });

    const answer = [];
    const map_report = new Map();
    const map_check = new Map();

    for (let r of reports) {
        map_report.set(r[0], condition ? [...condition, r[1]] : [r[1]]);
        map_check.set(r[1], map_check.get(r[1]) + 1 || 1);
    }

    for (let id of id_list) {
        let count = 0;
        for (let idx in map_report.get(id)) {
            if (map_check.get(map_report.get(id)[idx]) >= k) {
                count += 1;
            }
        }
        answer.push(count);
    }
    return answer;
}

function solution(id_list, report, k) {
    const reports = [...new Set(report)].map((r) => r.split(" "));
    const map_report = new Map();
    const map_check = new Map();

    for (let r of reports) {
        map_check.set(r[1], map_check.get(r[1]) + 1 || 1);
    }

    for (let r of reports) {
        if (map_check.get(r[1]) >= k) {
            map_report.set(r[0], map_report.get(r[0]) + 1 || 1);
        }
    }

    return id_list.map((id) => map_report.get(id) || 0);
}
