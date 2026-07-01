"use client";

import { useEffect, useState } from "react";
import { getJobs, Job } from "@/services/jobs";

export default function JobsPage() {
  const [jobs, setJobs] = useState<Job[]>([]);
  const [loading, setLoading] = useState(true);

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
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold">
            Jobs Management
          </h1>

          <p className="text-gray-500">
            Manage all recruitment jobs.
          </p>
        </div>

        <button className="rounded-lg bg-blue-600 px-5 py-2 font-semibold text-white hover:bg-blue-700">
          + Create Job
        </button>
      </div>

      {/* Loading */}
      {loading && (
        <div className="rounded-xl bg-white p-8 text-center shadow">
          Loading Jobs...
        </div>
      )}

      {/* Empty */}
      {!loading && jobs.length === 0 && (
        <div className="rounded-xl bg-white p-8 text-center shadow">
          No Jobs Found
        </div>
      )}

      {/* Jobs Table */}
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
    </div>
  );
}