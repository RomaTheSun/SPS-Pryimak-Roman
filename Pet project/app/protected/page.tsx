"use client";

import { useAuth } from "@/lib/auth/context";
import { useRouter } from "next/navigation";
import { useEffect } from "react";
import TableManager from "@/components/tables/TableManager";

export default function ProtectedPage() {
    const { user, logout, isLoggedIn, loading } = useAuth();
    const router = useRouter();

    // All hooks must be called before any conditional returns
    useEffect(() => {
        if (!loading && !isLoggedIn) {
            router.replace("/auth/login");
        }
    }, [isLoggedIn, loading, router]);

    const handleLogout = () => {
        logout();
        router.push("/");
    };

    if (loading) {
        return (
            <main className="min-h-screen flex items-center justify-center p-6">
                <div className="text-center">
                    <p>Loading...</p>
                </div>
            </main>
        );
    }

    if (!isLoggedIn) {
        return (
            <main className="min-h-screen flex items-center justify-center p-6">
                <div className="text-center">
                    <h1 className="text-2xl font-semibold mb-2">
                        Access Denied
                    </h1>
                    <p className="text-gray-600 mb-4">
                        You need to be logged in to view this page.
                    </p>
                    <a
                        href="/auth/login"
                        className="text-blue-600 underline hover:text-blue-800"
                    >
                        Go to Login Page
                    </a>
                </div>
            </main>
        );
    }

    return (
        <main className="min-h-screen p-6">
            <div className="max-w-5xl mx-auto mb-6 flex items-center justify-between">
                <h1 className="text-2xl font-semibold">
                    Welcome, {user?.username}
                </h1>
                <button
                    onClick={handleLogout}
                    className="bg-red-600 text-white px-4 py-2 rounded hover:bg-red-700"
                >
                    Logout
                </button>
            </div>
            <TableManager />
        </main>
    );
}
