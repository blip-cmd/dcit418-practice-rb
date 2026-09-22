import { byId, type Attempt } from "./model";
export function MockHistory({
  attempts,
  onExport,
}: {
  attempts: Attempt[];
  onExport: (sessionId: string) => void;
}) {
  const papers = [
    ...new Set(
      attempts.filter((a) => a.mode === "mock").map((a) => a.sessionId),
    ),
  ].reverse();
  if (!papers.length) return null;
  return (
    <section className="breakdown">
      <h2>Mock history</h2>
      {papers.map((id) => {
        const rows = attempts.filter((a) => a.sessionId === id);
        const misses = rows.filter((a) => !a.correct);
        return (
          <details key={id} className="result-item">
            <summary>
              {new Date(
                Math.max(...rows.map((a) => a.timestamp)),
              ).toLocaleString()}
              <span>
                {rows.length - misses.length} / {rows.length}
              </span>
            </summary>
            <button
              className="secondary"
              onClick={(e) => {
                e.preventDefault();
                onExport(id);
              }}
            >
              Export this paper's results ↗
            </button>
            <div className="part-scores">
              {[1, 2, 3, 4, 5, 6].map((part) => (
                <div key={part}>
                  <span>Part {part}</span>
                  <strong>
                    {
                      rows.filter(
                        (a) =>
                          byId.get(a.questionId)!.part === part && a.correct,
                      ).length
                    }
                    /10
                  </strong>
                </div>
              ))}
            </div>
            <h3>{misses.length} missed questions</h3>
            {misses.map((a) => {
              const q = byId.get(a.questionId)!;
              return (
                <div className="history-row" key={a.id}>
                  <strong>{q.id}</strong>
                  <span>{q.source}</span>
                  <span>{q.week}</span>
                </div>
              );
            })}
          </details>
        );
      })}
    </section>
  );
}
