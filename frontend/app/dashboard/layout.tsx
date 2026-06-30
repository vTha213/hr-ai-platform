"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import {
  LayoutDashboard,
  BriefcaseBusiness,
  FileText,
  Users,
  Share2,
  LogOut,
} from "lucide-react";

const menu = [
  {
    name: "Dashboard",
    href: "/dashboard",
    icon: LayoutDashboard,
  },
  {
    name: "Jobs",
    href: "/dashboard/jobs",
    icon: BriefcaseBusiness,
  },
  {
    name: "JD Generator",
    href: "/dashboard/jd-generator",
    icon: FileText,
  },
  {
    name: "Candidates",
    href: "/dashboard/candidates",
    icon: Users,
  },
  {
    name: "Social Media",
    href: "/dashboard/social-media",
    icon: Share2,
  },
];

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const pathname = usePathname();

  return (
    <div className="min-h-screen bg-gray-100 flex">

      {/* Sidebar */}

      <aside className="w-72 bg-slate-900 text-white">

        <div className="p-6 border-b border-slate-700">

          <h1 className="text-2xl font-bold">
            HR AI Platform
          </h1>

          <p className="text-sm text-gray-300 mt-1">
            Recruitment Dashboard
          </p>

        </div>

        <nav className="p-4 space-y-2">

          {menu.map((item) => {

            const Icon = item.icon;

            return (
              <Link
                key={item.href}
                href={item.href}
                className={`flex items-center gap-3 rounded-lg px-4 py-3 transition
                ${
                  pathname === item.href
                    ? "bg-blue-600"
                    : "hover:bg-slate-800"
                }`}
              >
                <Icon size={20} />

                {item.name}
              </Link>
            );
          })}

        </nav>

        <div className="absolute bottom-6 left-4">

          <button className="flex items-center gap-3 text-red-400 hover:text-red-300">

            <LogOut size={20} />

            Logout

          </button>

        </div>

      </aside>

      {/* Main */}

      <main className="flex-1">

        <header className="bg-white shadow px-8 py-5 flex justify-between items-center">

          <div>

            <h2 className="text-2xl font-bold">
              HR Dashboard
            </h2>

            <p className="text-gray-500">
              AI Recruitment Management System
            </p>

          </div>

          <div className="flex items-center gap-4">

            <div className="w-11 h-11 rounded-full bg-blue-600 text-white flex items-center justify-center font-bold">

              HR

            </div>

          </div>

        </header>

        <section className="p-8">

          {children}

        </section>

      </main>

    </div>
  );
}