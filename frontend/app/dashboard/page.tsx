"use client";

const stats = [
  {
    title: "Total Jobs",
    value: 12,
    color: "bg-blue-500",
  },
  {
    title: "Candidates",
    value: 84,
    color: "bg-green-500",
  },
  {
    title: "Pending Review",
    value: 18,
    color: "bg-yellow-500",
  },
  {
    title: "Shortlisted",
    value: 6,
    color: "bg-purple-500",
  },
];

const jobs = [
  {
    title: "AI Engineer",
    status: "Active",
  },
  {
    title: "Python Developer",
    status: "Active",
  },
  {
    title: "Data Analyst",
    status: "Draft",
  },
];

const candidates = [
  {
    name: "John Doe",
    cv: 92,
    github: 88,
    linkedin: 90,
  },
  {
    name: "Sarah Smith",
    cv: 87,
    github: 84,
    linkedin: 91,
  },
  {
    name: "Alex Johnson",
    cv: 90,
    github: 95,
    linkedin: 86,
  },
];

export default function DashboardPage() {
  return (
    <div className="space-y-8">

      {/* Welcome */}

      <div className="bg-white rounded-xl shadow p-6">

        <h1 className="text-3xl font-bold">
          Welcome HR 👋
        </h1>

        <p className="text-gray-500 mt-2">
          AI Powered Recruitment Dashboard
        </p>

      </div>

      {/* Stats */}

      <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">

        {stats.map((item) => (
          <div
            key={item.title}
            className={`${item.color} text-white rounded-xl p-6 shadow`}
          >
            <p className="text-lg">
              {item.title}
            </p>

            <h2 className="text-4xl font-bold mt-3">
              {item.value}
            </h2>
          </div>
        ))}

      </div>

      {/* Quick Actions */}

      <div className="bg-white rounded-xl shadow p-6">

        <h2 className="text-2xl font-bold mb-5">
          Quick Actions
        </h2>

        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-4">

          <button className="bg-blue-600 text-white rounded-lg p-4 hover:bg-blue-700">
            + Create Job
          </button>

          <button className="bg-green-600 text-white rounded-lg p-4 hover:bg-green-700">
            AI JD Generator
          </button>

          <button className="bg-yellow-500 text-white rounded-lg p-4 hover:bg-yellow-600">
            Review Candidates
          </button>

          <button className="bg-purple-600 text-white rounded-lg p-4 hover:bg-purple-700">
            Social Media Assets
          </button>

        </div>

      </div>

      <div className="grid lg:grid-cols-2 gap-8">

        {/* Recent Jobs */}

        <div className="bg-white rounded-xl shadow p-6">

          <h2 className="text-2xl font-bold mb-5">
            Recent Jobs
          </h2>

          <table className="w-full">

            <thead>

              <tr className="border-b">

                <th className="text-left py-2">
                  Position
                </th>

                <th className="text-left py-2">
                  Status
                </th>

              </tr>

            </thead>

            <tbody>

              {jobs.map((job) => (

                <tr key={job.title} className="border-b">

                  <td className="py-3">
                    {job.title}
                  </td>

                  <td>

                    <span className="bg-green-100 text-green-700 px-3 py-1 rounded-full text-sm">

                      {job.status}

                    </span>

                  </td>

                </tr>

              ))}

            </tbody>

          </table>

        </div>

        {/* Candidate Ranking */}

        <div className="bg-white rounded-xl shadow p-6">

          <h2 className="text-2xl font-bold mb-5">
            Top Candidates
          </h2>

          <table className="w-full">

            <thead>

              <tr className="border-b">

                <th>Name</th>

                <th>CV</th>

                <th>GitHub</th>

                <th>LinkedIn</th>

                <th>Total</th>

              </tr>

            </thead>

            <tbody>

              {candidates.map((candidate) => {

                const total =
                  (
                    candidate.cv * 0.7 +
                    candidate.github * 0.15 +
                    candidate.linkedin * 0.15
                  ).toFixed(1);

                return (

                  <tr
                    key={candidate.name}
                    className="border-b text-center"
                  >

                    <td className="py-3 text-left">
                      {candidate.name}
                    </td>

                    <td>{candidate.cv}</td>

                    <td>{candidate.github}</td>

                    <td>{candidate.linkedin}</td>

                    <td className="font-bold text-blue-600">
                      {total}
                    </td>

                  </tr>

                );

              })}

            </tbody>

          </table>

        </div>

      </div>

    </div>
  );
}