"use client";

import { useState } from "react";

export default function SocialMediaPage() {
  const [jobTitle, setJobTitle] = useState("");
  const [post, setPost] = useState("");

  const generatePost = () => {
    setPost(`🚀 We're Hiring!

Position: ${jobTitle}

Join our growing team and build amazing AI-powered products.

✅ Competitive Salary
✅ Hybrid / Remote
✅ Career Growth
✅ Friendly Team

Apply Now!

#Hiring #Jobs #AI #Python #Developer`);
  };

  return (
    <div className="space-y-6">

      <div>
        <h1 className="text-3xl font-bold">
          Social Media Generator
        </h1>

        <p className="text-gray-500">
          Generate hiring posts for LinkedIn, Twitter and Facebook.
        </p>
      </div>

      <div className="rounded-xl bg-white p-6 shadow space-y-5">

        <input
          className="w-full rounded-lg border p-3"
          placeholder="Job Title"
          value={jobTitle}
          onChange={(e) => setJobTitle(e.target.value)}
        />

        <button
          onClick={generatePost}
          className="rounded-lg bg-blue-600 px-5 py-3 text-white"
        >
          Generate Post
        </button>

        {post && (
          <div className="rounded-lg bg-slate-100 p-5 whitespace-pre-wrap">
            {post}
          </div>
        )}

      </div>

    </div>
  );
}