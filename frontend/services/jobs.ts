import api from "./api";

export interface Job {
  id: number;
  title: string;
  department: string;
  location: string;
  employment_type: string;
  experience: string;
  skills: string;
  description: string;
  approved: boolean;
}

export const getJobs = async (): Promise<Job[]> => {
  const response = await api.get("/jobs");
  return response.data;
};

export const createJob = async (job: Omit<Job, "id" | "approved">) => {
  const response = await api.post("/jobs", job);
  return response.data;
};

export const deleteJob = async (id: number) => {
  await api.delete(`/jobs/${id}`);
};

export const updateJob = async (
  id: number,
  job: Job
) => {
  const response = await api.put(`/jobs/${id}`, job);
  return response.data;
};