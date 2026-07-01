"use client";

const candidates = [
  {
    id: 1,
    name: "Rahul Sharma",
    position: "Python Developer",
    experience: "3 Years",
    score: "92%",
    status: "Shortlisted",
  },
  {
    id: 2,
    name: "Priya Singh",
    position: "Frontend Developer",
    experience: "2 Years",
    score: "88%",
    status: "Interview",
  },
  {
    id: 3,
    name: "Amit Kumar",
    position: "Data Analyst",
    experience: "4 Years",
    score: "81%",
    status: "Review",
  },
];

export default function CandidatesPage() {
  return (
    <div className="space-y-6">

      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold">
            Candidates
          </h1>

          <p className="text-gray-500">
            Review all applicants with AI score.
          </p>
        </div>

        <button className="rounded-lg bg-blue-600 px-5 py-2 text-white">
          + Add Candidate
        </button>
      </div>

      <input
        placeholder="Search candidate..."
        className="w-full rounded-lg border p-3"
      />

      <div className="overflow-hidden rounded-xl bg-white shadow">

        <table className="w-full">

          <thead className="bg-gray-100">

            <tr>

              <th className="p-4 text-left">
                Name
              </th>

              <th>Position</th>

              <th>Experience</th>

              <th>AI Score</th>

              <th>Status</th>

              <th>Action</th>

            </tr>

          </thead>

          <tbody>

            {candidates.map((candidate) => (

              <tr
                key={candidate.id}
                className="border-t"
              >

                <td className="p-4 font-semibold">
                  {candidate.name}
                </td>

                <td>{candidate.position}</td>

                <td>{candidate.experience}</td>

                <td className="font-bold text-blue-600">
                  {candidate.score}
                </td>

                <td>

                  <span className="rounded bg-green-100 px-3 py-1 text-green-700">
                    {candidate.status}
                  </span>

                </td>

                <td>

                  <button className="rounded bg-blue-600 px-3 py-1 text-white">
                    View
                  </button>

                </td>

              </tr>

            ))}

          </tbody>

        </table>

      </div>

    </div>
  );
}