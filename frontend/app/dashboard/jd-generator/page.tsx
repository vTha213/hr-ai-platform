"use client";

import { useState } from "react";

export default function JDGeneratorPage() {
  const [jobTitle, setJobTitle] = useState("");
  const [skills, setSkills] = useState("");
  const [experience, setExperience] = useState("");
  const [jd, setJd] = useState("");

  const generateJD = () => {
    setJd(`
Job Title: ${jobTitle}

Experience: ${experience}

Required Skills:
${skills}

Responsibilities:
• Develop scalable applications.
• Collaborate with cross-functional teams.
• Write clean and maintainable code.
• Participate in code reviews.
• Deliver high-quality software.

Preferred Qualifications:
• Strong communication skills.
• Problem solving mindset.
• Experience with modern development tools.
`);
  };

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-bold">AI JD Generator</h1>
        <p className="text-gray-500">
          Generate professional Job Descriptions using AI.
        </p>
      </div>

      <div className="rounded-xl bg-white p-6 shadow space-y-5">

        <input
          className="w-full rounded-lg border p-3"
          placeholder="Job Title"
          value={jobTitle}
          onChange={(e) => setJobTitle(e.target.value)}
        />

        <input
          className="w-full rounded-lg border p-3"
          placeholder="Experience (Example: 2-4 Years)"
          value={experience}
          onChange={(e) => setExperience(e.target.value)}
        />

        <textarea
          rows={5}
          className="w-full rounded-lg border p-3"
          placeholder="Required Skills"
          value={skills}
          onChange={(e) => setSkills(e.target.value)}
        />

        <button
          onClick={generateJD}
          className="rounded-lg bg-blue-600 px-5 py-3 text-white"
        >
          Generate JD
        </button>

        {jd && (
          <div className="rounded-lg bg-slate-100 p-5 whitespace-pre-wrap">
            {jd}
          </div>
        )}

      </div>
    </div>
  );
}