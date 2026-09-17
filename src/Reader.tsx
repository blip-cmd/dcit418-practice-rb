import { useEffect, useState } from "react";
import Markdown from "react-markdown";
import remarkGfm from "remark-gfm";
import remarkMath from "remark-math";
import rehypeKatex from "rehype-katex";
import { byId, displayOption } from "./model";

const markdown = (text: string) => (
  <Markdown remarkPlugins={[remarkGfm, remarkMath]} rehypePlugins={[rehypeKatex]}>
    {text}
  </Markdown>
);

export function Reader({
  ids,
  onSeen,
}: {
  ids: string[];
  onSeen: (id: string) => void;
}) {
  const [index, setIndex] = useState(0);
  const q = byId.get(ids[index])!;
  function move(delta: number) {
    setIndex((i) => Math.max(0, Math.min(ids.length - 1, i + delta)));
  }
  useEffect(() => {
    onSeen(q.id);
  }, [q.id, onSeen]);
  useEffect(() => {
    const handler = (event: KeyboardEvent) => {
      const target = event.target as HTMLElement;
      if (
        event.altKey ||
        event.ctrlKey ||
        event.metaKey ||
        target.isContentEditable ||
        target.closest("input, textarea, select, pre")
      )
        return;
      if (event.key === "ArrowLeft" || event.key === "ArrowRight") {
        event.preventDefault();
        move(event.key === "ArrowRight" ? 1 : -1);
      }
    };
    window.addEventListener("keydown", handler);
    return () => window.removeEventListener("keydown", handler);
  }, [ids.length]);
  return (
    <>
      <div className="page-heading">
        <div className="eyebrow">READING MODE · NO QUIZ</div>
        <h1>Read with answers.</h1>
        <p>
          Read the question, answer, and explanation together. Reading marks a
          question as seen, without recording a scored attempt.
        </p>
      </div>
      <div className="reader-navigation" aria-label="Reading navigation">
        <button
          className="primary"
          disabled={index === 0}
          onClick={() => move(-1)}
        >
          ← Previous
        </button>
        <span aria-live="polite">
          Question {index + 1} of {ids.length}
          <small>Use ← / → arrow keys</small>
        </span>
        <button
          className="primary"
          disabled={index === ids.length - 1}
          onClick={() => move(1)}
        >
          Next →
        </button>
      </div>
      <section className="question-card">
        <div className="tags">
          <span>{q.id}</span>
          <span>Part {q.part}</span>
          <span>{q.week}</span>
          <span>{q.level}</span>
        </div>
        <div className="markdown question-body">{markdown(q.bodyMarkdown)}</div>
        {q.options.length > 0 && (
          <details>
            <summary>View all options</summary>
            <div className="markdown">
              <ul>
                {q.options.map((_, i) => (
                  <li key={i}>{markdown(displayOption(q, i))}</li>
                ))}
              </ul>
            </div>
          </details>
        )}
        <section className="feedback right">
          <h2>Answer</h2>
          <div className="markdown">
            {markdown(
              q.correctIndex === null
                ? q.correctText
                : displayOption(q, q.correctIndex),
            )}
            {q.acceptedAnswers.length > 0 && (
              <>
                <strong>Also accepted</strong>
                {markdown(q.acceptedAnswers.join("; "))}
              </>
            )}
            <strong>Reason</strong>
            {markdown(q.reason)}
            <strong>Tempting wrong answer</strong>
            {markdown(q.trap)}
            <strong>Source</strong>
            {markdown(q.sourceRef)}
            {q.workingMarkdown && (
              <>
                <strong>Working</strong>
                {markdown(q.workingMarkdown)}
              </>
            )}
            <details>
              <summary>How this was checked</summary>
              {markdown(q.checkMethod)}
            </details>
          </div>
        </section>
      </section>
    </>
  );
}
