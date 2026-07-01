"use client";

import { useEffect, useState } from "react";
import {
  getJobs,
  createJob,
  Job,
} from "@/services/jobs";

export default function JobsPage() {
  const [jobs, setJobs] = useState<Job[]>([]);
  const [loading, setLoading] = useState(true);

  const [showModal, setShowModal] = useState(false);

  const [form, setForm] = useState({
    title: "",
    department: "",
    location: "",
    employment_type: "",
    experience: "",
    skills: "",
    description: "",
  });

  useEffect(() => {
    loadJobs();
  }, []);

  const loadJobs = async () => {
    try {
      const data = await getJobs();
      setJobs(data);
    } catch (error) {
      console.error("Failed to load jobs", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold">
            Jobs Management
          </h1>

          <p className="text-gray-500">
            Manage all recruitment jobs.
          </p>
        </div>

        <button
          onClick={() => setShowModal(true)}
          className="rounded-lg bg-blue-600 px-5 py-2 font-semibold text-white hover:bg-blue-700"
        >
          + Create Job
        </button>
      </div>

      {loading && (
        <div className="rounded-xl bg-white p-8 text-center shadow">
          Loading Jobs...
        </div>
      )}

      {!loading && jobs.length === 0 && (
        <div className="rounded-xl bg-white p-8 text-center shadow">
          No Jobs Found
        </div>
      )}

      {!loading && jobs.length > 0 && (
        <div className="overflow-hidden rounded-xl bg-white shadow">
          <table className="w-full">
            <thead className="bg-gray-100">
              <tr>
                <th className="p-4 text-left">Title</th>
                <th>Department</th>
                <th>Location</th>
                <th>Employment</th>
                <th>Experience</th>
                <th>Status</th>
              </tr>
            </thead>

            <tbody>
              {jobs.map((job) => (
                <tr
                  key={job.id}
                  className="border-t hover:bg-gray-50"
                >
                  <td className="p-4 font-semibold">
                    {job.title}
                  </td>

                  <td>{job.department}</td>

                  <td>{job.location}</td>

                  <td>{job.employment_type}</td>

                  <td>{job.experience}</td>

                  <td>
                    <span
                      className={`rounded px-3 py-1 text-sm font-medium ${
                        job.approved
                          ? "bg-green-100 text-green-700"
                          : "bg-yellow-100 text-yellow-700"
                      }`}
                    >
                      {job.approved
                        ? "Approved"
                        : "Pending"}
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {showModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/40">
          <div className="w-full max-w-xl rounded-xl bg-white p-6 shadow-xl">
            <h2 className="mb-5 text-2xl font-bold">
              Create Job
            </h2>

            <input
              className="mb-3 w-full rounded border p-3"
              placeholder="Job Title"
              value={form.title}
              onChange={(e) =>
                setForm({
                  ...form,
                  title: e.target.value,
                })
              }
            />

            <input
              className="mb-3 w-full rounded border p-3"
              placeholder="Department"
              value={form.department}
              onChange={(e) =>
                setForm({
                  ...form,
                  department: e.target.value,
                })
              }
            />

            <input
              className="mb-3 w-full rounded border p-3"
              placeholder="Location"
              value={form.location}
              onChange={(e) =>
                setForm({
                  ...form,
                  location: e.target.value,
                })
              }
            />

            <input
              className="mb-3 w-full rounded border p-3"
              placeholder="Employment Type"
              value={form.employment_type}
              onChange={(e) =>
                setForm({
                  ...form,
                  employment_type: e.target.value,
                })
              }
            />

            <input
              className="mb-3 w-full rounded border p-3"
              placeholder="Experience"
              value={form.experience}
              onChange={(e) =>
                setForm({
                  ...form,
                  experience: e.target.value,
                })
              }
            />

            <textarea
              className="mb-3 w-full rounded border p-3"
              placeholder="Skills"
              value={form.skills}
              onChange={(e) =>
                setForm({
                  ...form,
                  skills: e.target.value,
                })
              }
            />

            <textarea
              className="mb-5 w-full rounded border p-3"
              placeholder="Description"
              value={form.description}
              onChange={(e) =>
                setForm({
                  ...form,
                  description: e.target.value,
                })
              }
            />

            <div className="flex justify-end gap-3">
              <button
                onClick={() => setShowModal(false)}
                className="rounded bg-gray-300 px-4 py-2"
              >
                Cancel
              </button>

              <button
                onClick={() => setShowModal(false)}
                className="rounded bg-blue-600 px-4 py-2 text-white"
              >
                Save
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}