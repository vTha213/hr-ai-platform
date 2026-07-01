"use client";

export default function JobsPage() {
  const jobs = [
    {
      id: 1,
      title: "Python AI Developer",
      location: "Noida",
      type: "Full Time",
      applicants: 12,
      status: "Open",
    },
    {
      id: 2,
      title: "Frontend React Developer",
      location: "Delhi",
      type: "Hybrid",
      applicants: 8,
      status: "Open",
    },
    {
      id: 3,
      title: "Data Analyst",
      location: "Remote",
      type: "Remote",
      applicants: 21,
      status: "Closed",
    },
  ];

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

        <button className="rounded-lg bg-blue-600 px-5 py-2 text-white">
          + Create Job
        </button>
      </div>

      <div className="rounded-xl bg-white shadow">
        <table className="w-full">
          <thead className="bg-gray-100">
            <tr>
              <th className="p-4 text-left">Position</th>
              <th>Location</th>
              <th>Type</th>
              <th>Applicants</th>
              <th>Status</th>
            </tr>
          </thead>

          <tbody>
            {jobs.map((job) => (
              <tr
                key={job.id}
                className="border-t"
              >
                <td className="p-4 font-semibold">
                  {job.title}
                </td>

                <td>{job.location}</td>

                <td>{job.type}</td>

                <td>{job.applicants}</td>

                <td>
                  <span className="rounded bg-green-100 px-3 py-1 text-green-700">
                    {job.status}
                  </span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}