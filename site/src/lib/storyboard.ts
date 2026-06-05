export type StoryboardRow = {
  slide: number;
  module: string;
  actionTitle: string;
  coreContent: string;
  visualIntent: string;
  dataCodeAsset: string;
  teacherExplanation: string;
  studentAction: string;
  timing: string;
  textbookSectionLink: string;
  evidenceSourceNote: string;
  riskBoundaryNote: string;
};

export type StoryboardReviewMetrics = {
  rowCount: number;
  completeStudentActions: number;
  missingStudentActions: number;
  totalMinutes: number;
  duplicateActionTitles: number;
  maxTeacherRepeat: number;
  shortRows: number;
  genericEvidenceRows: number;
};

const FIELD_MAP: Record<string, keyof StoryboardRow> = {
  Slide: 'slide',
  Module: 'module',
  'Action title': 'actionTitle',
  'Core content': 'coreContent',
  'Visual intent': 'visualIntent',
  'Data/code asset': 'dataCodeAsset',
  'Teacher explanation': 'teacherExplanation',
  'Student action': 'studentAction',
  Timing: 'timing',
  'Textbook section link': 'textbookSectionLink',
  'Evidence/source note': 'evidenceSourceNote',
  'Risk/boundary note': 'riskBoundaryNote'
};

function splitRow(line: string) {
  return line
    .trim()
    .replace(/^\|/, '')
    .replace(/\|$/, '')
    .split('|')
    .map((cell) => cell.trim().replace(/<br>/g, '\n'));
}

function timingMinutes(value: string) {
  const match = value.match(/^\s*(\d+)\s*min\s*$/);
  return match ? Number(match[1]) : 0;
}

export function parseStoryboardRows(markdown: string): StoryboardRow[] {
  const lines = markdown.split(/\r?\n/);
  const headerLine = lines.find((line) => line.startsWith('| Slide |'));
  if (!headerLine) return [];
  const headers = splitRow(headerLine);

  return lines
    .filter((line) => /^\|\s*\d+\s*\|/.test(line))
    .map((line) => {
      const cells = splitRow(line);
      const row: Partial<StoryboardRow> = {};
      headers.forEach((header, index) => {
        const key = FIELD_MAP[header];
        if (!key) return;
        if (key === 'slide') {
          row.slide = Number(cells[index]);
        } else {
          row[key] = cells[index] as never;
        }
      });
      return row as StoryboardRow;
    });
}

export function storyboardReviewMetrics(rows: StoryboardRow[]): StoryboardReviewMetrics {
  const actionTitles = rows.map((row) => row.actionTitle).filter(Boolean);
  const teacherNotes = rows.map((row) => row.teacherExplanation).filter(Boolean);
  const uniqueTitles = new Set(actionTitles);
  const teacherCounts = teacherNotes.map((note) => teacherNotes.filter((candidate) => candidate === note).length);

  return {
    rowCount: rows.length,
    completeStudentActions: rows.filter((row) => row.studentAction).length,
    missingStudentActions: rows.filter((row) => !row.studentAction).length,
    totalMinutes: rows.reduce((sum, row) => sum + timingMinutes(row.timing), 0),
    duplicateActionTitles: actionTitles.length - uniqueTitles.size,
    maxTeacherRepeat: teacherCounts.length ? Math.max(...teacherCounts) : 0,
    shortRows: rows.filter((row) =>
      `${row.coreContent} ${row.teacherExplanation} ${row.studentAction} ${row.evidenceSourceNote} ${row.riskBoundaryNote}`.length < 120
    ).length,
    genericEvidenceRows: rows.filter((row) => {
      const note = row.evidenceSourceNote.trim();
      return !note || (!note.includes('/') && !note.includes('\\') && !note.includes('.'));
    }).length
  };
}
